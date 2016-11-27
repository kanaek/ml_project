import pandas as pd
import numpy as np
import pickle

class SubmissionCreator(object):

    def create_id(self, row):
        date = row["date"]
        sno = row["store_nbr"]
        ino = row["item_nbr"]
        id = "{}_{}_{}".format(sno, ino, date)
        return id

    def create_id2(self, row):
        date = row["date"]
        s_no = row["store_nbr"]
        i_no = row["item_nbr"]
        id = str(i_no) + "_" + str(s_no) + "_" + date[0:4] + date[5:7] + date[8:10]
        return id

    def create_prediction_dict(self, fname_test, fname_p):
        d = dict()

        f_test = open(fname_test)
        f_p = open(fname_p)
        lines_test = f_test.readlines()
        lines_p = f_p.readlines()

        for line_test, line_p in zip(lines_test, lines_p):
            p_from_baseline = float(line_p.strip())

            I = line_test.strip().split("|")[-1]
            id2 = I.split(" ")[2]
            notsold = I.split(" ")[4]
            baseline = float(I.split(" ")[-1])

            if notsold == "True":
                pred = p_from_baseline + baseline
            else:
                pred = 0.0

            d[id2] = np.max([pred, 0.0])

        return d

    def create_submission(self, df_test, df_submission,fname_submission):
        df = df_test
        dict = {}
        df_sub = df_submission.copy()
        fw = open(fname_submission, "w")
        fw.write("id,units\n")

        for index, row in df.iterrows():
                id = self.create_id(row)
                dict[id] = row['units']

        for index1,row1 in df_sub.iterrows():
            k  = row1['id']
            if dict.has_key(k):
                #row1['units'] = dict[k]
                #print row1['units']
                fw.write("{},{}\n".format(k, dict[k]))
            else:
                fw.write("{},{}\n".format(k, 0))
        print "finished {}".format(fname_submission)


submission_creator = SubmissionCreator()
df_test = pd.read_csv("model/test_re.csv")
df_sub = pd.read_csv("submission/sampleSubmission.csv")
#prediction_dict = submission_creator.create_prediction_dict("model/vwdata_test.vwtxt", "model/vwdata.predict.txt")
submission_creator.create_submission(df_test,df_sub, "submission/q.csv")