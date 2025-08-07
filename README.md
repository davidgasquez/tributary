# Tributary 🌊

> Credibly neutral data marketplace where contributors earn token rewards for curating high-value datasets.

Tributary is an open protocol for running data competitions where participants earn rewards for contributing valuable training data. Unlike traditional ML competitions where models compete on fixed data, Tributary fixes the model and evaluation set while participants compete by submitting better training datasets.

## How It Works

1. **Competition Setup**: Hosts create a competition with a fixed model and private test set.
2. **Data Submission**: Participants submit training datasets via encrypted files.
3. **Evaluation**: Submissions are evaluated using leave-one-provider-out or KNN Shapley.
4. **Rewards**: Contributors earn rewards proportional to their marginal data value.

## Contribute a Dataset

To protect data confidentiality and enable fair evaluation, all training data must be encrypted before submission:

1. Download the public PGP key (`public.asc`) from this repository
2. Encrypt your training data file using the public key:
   ```bash
   gpg --armor --encrypt --recipient-file public.asc train.csv
   ```
3. This creates an encrypted file `train.csv.asc` that only competition hosts can decrypt
4. Submit the URL of the encrypted file to the competition `submissions.yaml` file

## License

MIT License - see [LICENSE](LICENSE) for details.
