# DSC-2023
## Group B - UIT Data Science Challenge 2023 on the task of Fact Checking &amp; Verification
- I split notebooks into Public and Private to clarify which notebooks I used in each phase.
- The training dataset was so large that I could not upload it here.
- We fine-tuned the XLM-R model (pretrained from Huggingface), we also modified MultiVerS's architecture by replacing its own Longformer with Longformer-PhoBERT and trained it from scratch.
- We did inference results with XLM-R first, then we used MultiVerS to double check the results as MultiVers could handle NEI cases so well but not the others.
- Our team achieved top 3 in public scoreboard and top 10 in private scoreboard.
