from sqlalchemy.engine.default import DefaultDialect
from sqlalchemy.engine.default import DefaultExecutionContext
from sqlalchemy.connectors.pyodbc import PyODBCConnector


class FM11ExecutionContext(DefaultExecutionContext):

	def get_lastrowid(self):

		# *sigh* .. maybe some day when FileMaker pulls it's something
		# out of something...

		#cursor = self.create_cursor()
		#cursor.execute('SELECT effin_filemaker_autoenter_rowid()')
		#lastrowid = cursor.fetchone()[0]
		#cursor.close()
		#return lastrowid

		return False

class FM11Dialect(DefaultDialect):
	execution_ctx_cls = FM11ExecutionContext

	def __init__(self, *args, **kwargs):
		DefaultDialect.__init__(self, *args, **kwargs)

		self.convert_unicode = True

class dialect(PyODBCConnector, FM11Dialect):
	name='fm11'

	supports_unicode_statements = False

	# FM11 ODBC gives a query syntax error for the unicode return test
	def _check_unicode_returns(self, conn):
		return False

	def do_execute(self, cursor, statement, parameters, context=None):
		# remove unicode if present
		if isinstance(statement, unicode):
			statement = statement.encode(self.encoding)
		cursor.execute(statement, parameters)

