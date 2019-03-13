        logloss = log_loss(y_true, y_pred)
        acc = accuracy_score(y_true, y_pred_label)
        precision = precision_score(y_true, y_pred_label, average='micro')
        recall = recall_score(y_true, y_pred_label, average='micro')
        f1 = f1_score(y_true, y_pred_label, average='micro')
        fpr, tpr, thresholds = roc_curve(y_true, y_pred)
        auc_score = auc(fpr, tpr)

        metrics = [logloss,
                   acc,
                   auc_score,
                   precision,
                   recall,
                   f1]