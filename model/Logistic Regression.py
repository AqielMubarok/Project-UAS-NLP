#Here I choose C=1 to build the final model for Logistic Regression
final_model_lr = LogisticRegression(C=1)
final_model_lr.fit(X, y)
print('Final Model Accuracy: %s' %accuracy_score(y_test, final_model_lr.predict(X_test)))
Final Model Accuracy: 0.9475138121546961