var express = require('express'),
    app = express(),
    port = process.env.PORT || 9000,
    bodyParser = require('body-parser'),
    cors = require('cors'),
    controller = require('./contactcontroller'),
    server = require('http').createServer(app),
    socket = require('socket.io');


app.set('view engine', 'ejs');
app.use(cors());
app.use(express.static(__dirname + '/pages'));
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

var routes = require('./routes');
routes(app);

// io.on('connection', function (socket) {
//     console.log('a user connected');
// });
const io = socket(server)
var connection = require('./connect')
io.sockets.on('connection', function (socket) {
    //console.log('a client connected');
    sendData(socket);
});
var data = []
function sendData(socket){
    connection.query('SELECT * FROM smartp ORDER BY masuk DESC LIMIT 1', function (err, rows) {
        if (err) throw err;
        //console.log('Data received from Db:\n');
        //console.log(rows);
        if (rows.length > 0)
            data[0] = rows[0]
    });
    connection.query('SELECT * FROM smartp WHERE keluar > 0 ORDER BY masuk DESC LIMIT 1', function (err, rows) {
        if (err) throw err;
        //console.log('Data received from Db:\n');
        // console.log(rows);
        if (rows.length > 0)
            data[0].keluar = rows[0].keluar
    });
        socket.emit('showrows', data);
    setTimeout(() => {
        sendData(socket)
    }, 10);
}
//app.listen(port);
server.listen(port, function () {
    console.log('Learn Node JS , RESTful API server started on: ' + port);
});