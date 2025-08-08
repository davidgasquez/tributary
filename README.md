# Tributary 🌊

Credibly neutral data marketplace where contributors earn token rewards for curating high-value datasets. Participants compete by sending datasets that improve the evaluation metrics on a fixed model and test set.

## 🥇 Leaderboard

| Rank | Contributor | Accuracy |
| ---- | ----------- | -------- |
| 1    | alice         | 0.8249   |

## 🛠️ How It Works

1. **Competition Setup**: Hosts create a competition repository with a fixed model and a private test set
2. **Data Submission**: Participants submit training encrypted datasets for training
3. **Evaluation**: Submissions are evaluated using leave-one-provider-out or KNN Shapley
4. **Rewards**: Contributors earn rewards proportional to their marginal data value

## 📊 Quickstart

Sending a new dataset is easy.

1. Download `public.asc` from this repository
2. Encrypt your dataset (training data) with `gpg --armor --encrypt --recipient-file public.asc train.csv`
3. Host the file somewhere
4. Send a Pull Requests adding the URL of the encrypted `.asc` file to `submissions.yaml`

## 📜 License

MIT License - see [LICENSE](LICENSE) for details.
