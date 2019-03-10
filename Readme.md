![Mongo DB](https://cdn-images-1.medium.com/max/1200/1*Mx3MUKkPENbaIR-vKGeLDw.jpeg)
<h1>Analytics in MongoDB</h1>

```
CRUD                                  Analytics
CREATE ---------> Database  ---------> Group
READ   ---------> (MongoDB) ---------> COUNT
UPDATE --------->           ---------> DERIVE VALUES
DELETE --------->           ---------> FILTER, AVERAGE, SORT
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

```
$match -----> $project -----> $group -----> $sort
```

</ul>

<h3>Rich Library of functions</h3>
<ul>
    <li>Filter, compute, group, and summarize data</li>
    <li>Output of one stage sent to input of next</li>
    <li>Operation executed in sequential order</li>
</ul>

<h3>Syntax For an Aggregation</h3>

```
>db.foo.aggregate([{ stage1 },{ stage2 },{ stage3 }, .... ])
```

<ol>
    <li>db - variable pointing to current database</li>
    <li>collection name</li>
    <li>agggregate - method on collection</li>
    <li>array of objects, each a pipeline operator</li>
    <li>pipeling operators</li>
</ol>

<h3>Some Popular Pipeline Operators</h3>

```
    $match       ---> Filter documents
    $project     ---> Reshape documents
    $group       ---> Summarize documents
    $unwind      ---> Expand arrays in documents
    $sort        ---> Order documents
    $limit/$skip ---> Paginate documents
    $redact      ---> Restrict documents
    $geoNear     ---> Proximity sort documents
    $let,$map    ---> Define variables
```
