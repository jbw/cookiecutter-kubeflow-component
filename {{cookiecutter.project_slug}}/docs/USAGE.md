
### Run train test split

```sh
python train_test_split.py --model-build-id 0 --training-data-s3-path "transaction-parties/transaction-parties-2000.csv" --s3-bucket-name "test-data" --test-size 0.2
 ```

### Build preprocess

Preprocess test data

```sh
 python preprocess.py --model-build-id=1 --features-file-path=.experiments/test_features.csv  --labels-file-path=.experiments/test_labels.csv --output-train-labels-file-path=".experiments/test_preprocessed_labels.csv" --output-train-features-file-path=".experiments/test_preprocessed_features.csv"
```

Preprocess training data

```sh
python preprocess.py --model-build-id=1 --features-file-path=".experiments/train_features.csv"  --labels-file-path=".experiments/train_labels.csv" --output-train-labels-file-path=".experiments/train_preprocessed_labels.csv" --output-train-features-file-path=".experiments/train_preprocessed_features.csv"
```
### Build train

```sh
python train.py --model-build-id=1 --s3-bucket-name="test-data"  --training-labels-s3-path=".experiments/train_preprocessed_labels.csv" --training-features-s3-path=".experiments/train_preprocessed_features.csv" --char-index-lookup-s3-path=".experiments/char_to_index_lookup.json" --output-classifier-file-path=".experiments/classifier" 

```

### Build model validation

 ```sh
 python model_validation.py --model-build-id 1 --features-file-path=".experiments/preprocessed_features.csv" --labels-file-path=".experiments/preprocessed_labels.csv" --classifier-file-path=".experiments/classifier/"
 ```

### Run prediction 

 ```sh
 python predict.py --model-build-id 1 --features-file-path=".experiments/test_preprocessed_features.csv" --classifier-file-path=".experiments/classifier/"
 ```


### Build pipeline

 ```sh
 python pipeline/pipeline.py
 ```
