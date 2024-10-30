A complete End-to-End Machine Learning Project

1) Firstly i setup my project repo in git and able to connect the vscode to git to make the changes in the files easily. I established various files like setup.py, requirements.txt to get the packages installed on their own. setup.py contains code that gets our required packages and the text file contains the names of the packages.

2) We need to create a component folder which holds the modules of the project.It contains files like data_ingestion.py(get data from the sources), data_trasformation.py(making data ready for the model), model_trainer.py(from the available data we build the model).This step makes the project clear and navigate with ease. Now we also create a folder 'pipeline' which contains files train_pipeline.py(useful to do all the training part easily), predict_pipeline.py(similar to train_pipeline.py but here we predict the outcome from the trained model).
