var express = require('express');
var app = express();
var BodyParser = require('body-parser');
var shell = require('shelljs');
var fs = require('fs');

app.set("view engine","ejs");
app.use(express.static('public'));
app.use(BodyParser.urlencoded({extended:true}));

app.get("/", function(req, res){
    res.render("home.ejs");
});

app.post("/survey", function(req, res){
    var pnr = req.body.pnr;
    console.log("PNR_Validated")
    res.render("survey.ejs", {pnr_value : pnr} );
});

app.post("/book", function(req, res){
    
    //var values = req.body.values.scores;
    //var temp = {val : values};
    //var jsonObj = JSON.stringify(temp);
    //fs.writeFileAsync('myFile.json', jsonObj);
    //shell.exec('python Prediction.py');
    //fs.readFile('output.txt', 'utf8', function(err, contents) {
    
    console.log("Prediction_Validated")
    console.log("3.0")
    res.render("Booking.ejs")
});

app.listen(3000, function(){
    console.log("Server is Running");
});

