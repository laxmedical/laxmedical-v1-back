const https = require('https'),
    fs = require("fs");
const express = require('express');
const { ExpressPeerServer } = require('peer');

const app = express();

app.get('/', (req, res, next) => res.send('Hello world!'));

// =======
app.listen(9009);
sslOptions = {
    key: fs.readFileSync('C:\\OpenSSL\\privateKey.key'),
    cert: fs.readFileSync('C:\\OpenSSL\\certificate.crt')
}

const server = https.createServer(sslOptions, app).listen(9000);

const peerServer = ExpressPeerServer(server, {
    path: '',
    ssl: {
        key: fs.readFileSync('C:\\OpenSSL\\privateKey.key'),
        cert: fs.readFileSync('C:\\OpenSSL\\certificate.crt')
    }
});

var connected = [];
peerServer.on('connection', function(id) {
    var idx = connected.indexOf(id); // only add id if it's not in the list yet
    if (idx === -1) { connected.push(id); }
});
peerServer.on('disconnect', function(id) {
    var idx = connected.indexOf(id); // only attempt to remove id if it's in the list
    if (idx !== -1) { connected.splice(idx, 1); }
});

app.get('/connected-people', function(req, res) {
    return res.json(connected);
});

app.use('/peerjs', peerServer);