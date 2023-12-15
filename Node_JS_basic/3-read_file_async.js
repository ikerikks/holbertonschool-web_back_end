const fs = require('fs');

async function countStudents(path) {
  const promesa = new Promise((resolve, reject) => {
    fs.readFile(path, 'utf-8', (err, res) => {
      if (err) {
        reject(err);
      }
      resolve(res);
    });
  });

  promesa
    .then((data) => {
      const strData = data.trim().split('\n');
      strData.shift();
      // console.log(data);
      const studentsCS = strData.filter((val) => val.includes('CS')).map((student) => student.split(','));
      const studentsSWE = strData.filter((val) => val.includes('SWE')).map((student) => student.split(','));

      console.log(`Number of students: ${strData.length}`);
      console.log(
        `Number of students in CS: ${studentsCS.length}. `
        + `List: ${studentsCS.map((val) => val[0]).join(', ')}`,
      );
      console.log(
        `Number of students in SWE: ${studentsSWE.length}. `
        + `List: ${studentsSWE.map((val) => val[0]).join(', ')}`,
      );
    })
    .catch(() => {
      throw new Error('Cannot load the database');
    });
  return promesa;
}

module.exports = countStudents;
