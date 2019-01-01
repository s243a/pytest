
//var script = document.createElement('script');

//script.src = '//code.jquery.com/jquery-1.11.0.min.js';
//document.getElementsByTagName('head')[0].appendChild(script); 

//$.post("demo_test.asp", function(data, status){
//       alert("Data: " + data + "\nStatus: " + status);
//
//$("button").click(function(){
//    $.post("demo_test.asp", function(data, status){
//        alert("Data: " + data + "\nStatus: " + status);
//    });
//});

//https://stackoverflow.com/questions/1255948/post-data-in-json-format
// construct an HTTP request
//xhr.open(form.method, form.action, true);
//var xhr = require('/usr/lib/nodejs/xmlhttprequest').XMLHttpRequest;
var xhr = new XMLHttpRequest();
//var xhr = bla.XMLHttpRequest();
xhr.open("post", "/KSK/insert", true);
xhr.setRequestHeader('Content-Type', 'application/json; charset=UTF-8');
console.log("hi");
xhr.onreadystatechange  = function () {
    //document.write(xhr.responseText)
    //console.log(xhr.responseTex)
    print(xhr.responseTex);
};
  // send the collected data as JSON
xhr.send(JSON.stringify(data));
