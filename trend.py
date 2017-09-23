import time

import algos.lstm as lstm

import plotter as pt


def getTrends(file_path,epochs):
    global_start_time = time.time()
    seq_len = 50

    print('> Loading data... ')

    X_train, y_train, X_test, y_test = lstm.load_data(file_path, seq_len, True)

    print('> Data Loaded. Compiling...')

    model = lstm.build_model([1, 50, 100, 1])

    model.fit(
        X_train,
        y_train,
        batch_size=512,
        nb_epoch=epochs,
        validation_split=0.05)

    predictions = lstm.predict_sequences_multiple(model, X_test, seq_len, 50)
    # predicted = lstm.predict_sequence_full(model, X_test, seq_len)
    # predicted = lstm.predict_point_by_point(model, X_test)

    print('Training duration (s) : ', time.time() - global_start_time)
    pt.plot_results_multiple(predictions, y_test, 50)
