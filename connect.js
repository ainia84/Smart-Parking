var mysql = require('mysql');

var con = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "Ainiaalif123",
  database: "parkir"
});

con.connect(function (err){
    if(err) throw err;
});


module.exports = con;