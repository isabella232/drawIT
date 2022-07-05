var express = require('express');
var fs = require('fs');
var unzipper = require('unzipper');
var { execFile } = require("node:child_process");
var router = express.Router();

router.post('/drawit/:id', function(request, response, next) {
  let buffers = [];

  request.on('data', function(data) {
    buffers.push(data);
  });

  request.on('end', function() {
    let buffer = Buffer.concat(buffers);
    let savepath = "./downloads/";
    //let savepath = "/tmp/downloads/";
    let timestamp = Date.now();

    let accountstamp = "account" + request.params.id + "-" +  timestamp.toString();
    let accountpath = savepath + accountstamp + "/";
    var inputzip = accountpath + "account.zip";
    var inputname = accountpath + "account.json";
    var outputname = accountpath + "account.xml";
    var logname = accountpath + "errors.log";
    var combinedname = accountpath + "combined.xml";

    if (!fs.existsSync(savepath)) fs.mkdirSync(savepath);
    if (!fs.existsSync(accountpath)) fs.mkdirSync(accountpath);

    fs.writeFile(inputzip, buffer, (error) => {
      if (error)
        console.log("drawIT unable to save file " + inputzip);
    });

    fs.createReadStream(inputzip)
      .pipe(unzipper.Extract({ path: accountpath } ))
      .on('finish', function() { 
        fs.readdir(accountpath, function(error, files) {
          if (error)
            console.log("drawIT unable to read directory " + accountpath);
          else {
	    for (let index = 0; index < files.length; index++) {
	      let file = files[index];
	      let segments = file.split(".");
	      let type = segments.pop();
	      if (type == 'json' || type === 'yaml' || type === 'yml') {
	        inputname = accountpath + file;
	        outputname = accountpath + segments[0] + '.xml';
                break;
	      }
	    }
          }

          drawIT(request, response, accountpath, inputname, outputname, logname, combinedname);
        });
      });
  })
});

function drawIT(request, response, accountpath, inputname, outputname, logname, combinedname) {
  console.log("drawIT starting with input from " + inputname);

  const child = execFile('python3', ['./drawit.py', '-input', inputname, '-output', accountpath, '-mode', 'web'], (error, stdout, stderr) => {
    if (error) throw error;
    fs.writeFile(logname, stderr, (error) => {
      if (error)
        console.log("drawIT unable to save file " + logname);

      // Combine log and xml file.
      fs.appendFileSync(outputname, "\n\n<!-- BEGIN Error Log\n" + stderr + "END Error Log -->\n", (error) => {
        if (error)
          console.log("drawIT unable to append file " + outputname);
      });

      response.sendFile(outputname, { root: '.' }, function(error) {
        if (error)
          console.log("drawIT unable to send file " + outputname);
        else 
	  console.log("drawIT sent response with file " + outputname);
      });
    });

    console.log("drawIT completed with output to " + outputname);
  });
}

module.exports = router;
