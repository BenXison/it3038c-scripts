//Another possible way to output to HTML
const express = require('express');
const app = express();
var host = "localhost";
var port = 8000;


app.get('/', (req, res) => {
    //get hostname
    const os = require('os');
    const HostName = '<h1>Hostname: ' + os.hostname() + '</h1>';
    //get ip address
    var ip = require("ip");
    const IPaddress = '<h1>IP Address: ' + ip.address() + '</h1>';

    //Get Server Uptime
    let ut_sec = os.uptime();
    let ut_min = ut_sec / 60;
    let ut_hour = ut_min / 60;
    let ut_day = ut_hour / 24;

    ut_sec = Math.floor(ut_sec);
    ut_min = Math.floor(ut_min);
    ut_hour = Math.floor(ut_hour);
    ut_day = Math.floor(ut_day);

    ut_day = ut_day % 24;
    ut_hour = ut_hour % 60;
    ut_min = ut_min % 60;
    ut_sec = ut_sec % 60;
    const serverUptime = '<h1>Server Uptime: ' + "Up time: " + ut_day + " Day(s) " + ut_hour + " Hour(s) "	+ ut_min + " minute(s) and " + ut_sec + " second(s)" + '</h1>';

    //Get Total Memory and Free Memory
    const totalMemory = (Math.trunc(os.totalmem()/ (1024 ** 2)));
    const tmemory = '<h1>Total Memory: ' + totalMemory + ' MB </h1>';

    //Get free memory
    const freeMemory = (Math.trunc(os.freemem()/ (1024 ** 2)));
    const fmemory = '<h1>Free Memory: ' + freeMemory + ' MB </h1>';

    //Count CPUs
    const cpuCount = os.cpus().length;
    const TotalCPU = '<h1>CPUs: ' + cpuCount + '</h1>';

    res.write(HostName)
    res.write(IPaddress)
    res.write(serverUptime)
    res.write(tmemory)
    res.write(fmemory)
    res.write(TotalCPU)
    res.send();
});

app.listen(8000, () => {
    console.log(`Server is running on http://${host}:${port}`);
});
