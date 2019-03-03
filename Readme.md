<h1>Analytics in MongoDB</h1>

CRUD Analytics

```
CREATE ---------> Database ---------> Group
READ ---------> (MongoDB) ---------> COUNT
UPDATE ---------> ---------> DERIVE VALUES
DELETE ---------> ---------> FILTER, AVERAGE, SORT
```

<h1>Core Concept : Pipeline</h1>

```
ls -1 ---------> Pipe ---------> wc -l --------->   Terminal
       stdout           stdin            stdout
```

Ex : ps -ef | grep mongod
