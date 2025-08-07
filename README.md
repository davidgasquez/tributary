# Tributary 🌊

Data marketplace where contributors earn rewards for curating datasets. Unlike traditional ML competitions where models compete on fixed data, Tributary fixes the model while participants compete by submitting better training datasets.

## How It Works

1. **Competition Setup**: Hosts create a competition with a fixed model and private test set
2. **Data Submission**: Participants submit training datasets via encrypted files
3. **Evaluation**: Submissions are evaluated using leave-one-provider-out or KNN Shapley
4. **Rewards**: Contributors earn rewards proportional to their marginal data value

## Contribute a Dataset

All training data must be encrypted before submission:

1. Download `public.asc` from this repository
2. Encrypt your training data with `gpg --armor --encrypt --recipient-file public.asc train.csv`
3. Send a Pull Requests adding the URL of the encrypted `.asc` file to `submissions.yaml`

## 📜 License

MIT License - see [LICENSE](LICENSE) for details.
