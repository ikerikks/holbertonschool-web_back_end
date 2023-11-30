const fs = require('fs');
function countStudents(path) {
  let data = fs.readFileSync(`${path}`, 'utf-8').split('\n');
  data.shift();
  let studentsCS = data.filter(val => val.includes('CS')).map((student) => student.split(','));
  let studentsSWE = data.filter(val => val.includes('SWE')).map((student) => student.split(','));
  
  console.log(`Number of students ${data.length}`);
  console.log(
    `Number of students in CS ${studentsCS.length} ` + 
    `List: ${studentsCS.map((val) => val[0]).join(', ')}`
    );

  console.log(
    `Number of students in SWE ${studentsSWE.length} ` +
    `List: ${studentsSWE.map((val) => val[0]).join(', ')}`
    );

}

module.exports = countStudents;
