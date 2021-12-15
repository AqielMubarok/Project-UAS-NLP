#Here I choose C=1 to build the final model for support vector
final_model_sv = SVC(C=1)
final_model_sv.fit(X, y)
print('Final Model Accuracy: %s' %accuracy_score(y_test, final_model_sv.predict(X_test)))
Final Model Accuracy: 0.9033149171270718