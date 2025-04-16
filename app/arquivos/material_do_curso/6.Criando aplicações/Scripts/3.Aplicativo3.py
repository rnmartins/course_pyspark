#Prof. Fernando Amaral
import sys, getopt
from pyspark.sql import SparkSession

if __name__ == "__main__":
        spark = SparkSession.builder.appName("Exemplo").getOrCreate()

        #parametros que requerem um argumento são seguidos de :
        opts, args = getopt.getopt(sys.argv[1:], "t:i:o:")

        formato, infile, outdir = "","",""


        for opt, arg in opts:
                if opt == "-t":
                   formato = arg
                 elif opt == "-i":
                   infile = arg
                elif opt == "-o":
                   outdir = arg

        dados = spark.read.csv(infile, header=False, inferSchema = True)
        dados.write.format(formato).save(outdir);


        spark.stop()
