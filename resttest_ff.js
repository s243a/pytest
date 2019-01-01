/*
 * This is a JavaScript Scratchpad.
 *
 * Enter some JavaScript, then Right Click or choose from the Execute Menu:
 * 1. Run to evaluate the selected text (Ctrl+R),
 * 2. Inspect to bring up an Object Inspector on the result (Ctrl+I), or,
 * 3. Display to insert the result in a comment after the selection. (Ctrl+L)
 */


var xhr = new XMLHttpRequest();
//var xhr = bla.XMLHttpRequest();
xhr.open("post", "http://127.0.0.1:8082/KSK/insert", true);
xhr.setRequestHeader('Content-Type', 'application/json; charset=UTF-8');
window.console.log("hi");
xhr.onreadystatechange  = function () {
    //document.write(xhr.responseText)
    window.console.log("Entering Callback")
    window.console.log(xhr.responseText)
    //print(xhr.responseText());
};

window.console.log("making json data")
var data={"message":"This is a test message",
          "ksk":"testtest123456789",
          "host":"192.168.1.2", //Optional argument. Default = "127.0.0.1"
          "port":9481}; //OPtional argument. Default = 9481
window.console.log("Ready to send");
  // send the collected data as JSON
xhr.send(JSON.stringify(data));



/*
undefined
*/
/*
undefined
*/