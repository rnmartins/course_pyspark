#Prof. Fernando Amaral
import sys, getopt
from pyspark.sql import SparkSession
if __name__ == "__main__":
	spark = SparkSession.builder.appName("Tabelas").getOrCreate()
	opts, args = getopt.getopt(sys.argv[1:], "a:t:")
	arquivo, tabela = "",""
	for opt, arg in opts:
		if opt == "-a":
			arquivo = arg
		elif opt == "-t":
			tabela = arg
	#le os dados
	df = spark.read.load(arquivo)
	#gravar dados no postgre
	df.write.format("jdbc").option("url","jdbc:postgresql://localhost:5432/tabelas").option("dbtable",tabela).option("user","postgres").option("password","123456").option("driver","org.postgresql.Driver").save()
	spark.stop()


