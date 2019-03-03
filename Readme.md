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

<h1>What is the Aggregation Pipeline?</h1>
<h3>A series of Document Transformations</h3>
<ul>
    <li>Executed in stages</li>
    <li>Original input is a collection</li>
    <li>Output as a cursor or a collection</li>
    <li> 
        ```
        $match -----> $project -----> $group -----> $sort
        ```
    </li>
</ul>

<h3>Rich Library of functions</h3>
<ul>
    <li>Filter, compute, group, and summarize data</li>
    <li>Output of one stage sent to input of next</li>
    <li>Operation executed in sequential order</li>
</ul>
