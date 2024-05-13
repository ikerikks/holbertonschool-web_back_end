import http from 'http';
import fs from 'fs';

const app = http.createServer(async (req, res) => {
  const promesa = await new Promise((resolve, reject) => {
    fs.readFile(process.argv[2], 'utf-8', (err, res) => {
      if (err) {
        reject(err);
      }
      const strData = res.trim().split('\n');
      strData.shift();
      const studentsCS = strData.filter((val) => val.includes('CS')).map((student) => student.split(','));
      const studentsSWE = strData.filter((val) => val.includes('SWE')).map((student) => student.split(','));
      let result =
        `Number of students: ${strData.length}\n`
        + `Number of students in CS: ${studentsCS.length}. `
        + `List: ${studentsCS.map((val) => val[0]).join(', ')}\n`
        + `Number of students in SWE: ${studentsSWE.length}. `
        + `List: ${studentsSWE.map((val) => val[0]).join(', ')}`
      ;
      resolve(result);
    });
  });

  // promesa
  //   .then((data) => {
  //     const strData = data.trim().split('\n');
  //     strData.shift();
  //     const studentsCS = strData.filter((val) => val.includes('CS')).map((student) => student.split(','));
  //     const studentsSWE = strData.filter((val) => val.includes('SWE')).map((student) => student.split(','));

  //     result =
  //       `Number of students: ${strData.length}`
  //       + `Number of students in CS: ${studentsCS.length}. `
  //       + `List: ${studentsCS.map((val) => val[0]).join(', ')}`
  //       + `Number of students in SWE: ${studentsSWE.length}. `
  //       + `List: ${studentsSWE.map((val) => val[0]).join(', ')}`
  //     ;
  //     // console.log("OK FINE");
  //     // console.log(result);
  //   })
  //   .catch((e) => {
  //     // console.log("ERROR ERROR");
  //     // console.log(e);
  //     // console.log("------------------");

  //     throw new Error('Cannot load the database');
  //   });
  
  switch (req.url) {
    case '/':
      res.write('Hello Holberton School!');
      break;
    case '/students':
      res.write('This is the list of our students\n' + promesa);
      
  }

  res.end();
}).listen(1245);

