from nemo.collections import nlp as nemo_nlp
import sys
model_path = "/home/val/HDD1/Repos/AI-Driven-Specialist-Matching-Model/nemo_experiments/specialist-matching/2026-04-01_13-14-59/checkpoints/specialist-matching.nemo"

model = nemo_nlp.models.IntentSlotClassificationModel.restore_from(model_path)

model.cuda()

buf = [""]
while(True):
    buf[0] = input("Prompt: ")

    if(buf[0] == "q"):
        sys.exit()

    pred_intents, pred_slots = model.predict_from_examples(buf, model.cfg.test_ds)

    for intent, slots in zip(pred_intents, pred_slots):
        print(f'Predicted Intent: {intent}')
        print(f'Predicted Slots: {slots}')
