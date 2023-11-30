const fs = require('fs');

function countStudents(path) {
  try {
    const data = fs.readFileSync(`${path}`, 'utf-8').trim().split('\n');
    // console.log(data);
    data.shift();
    const studentsCS = data.filter((val) => val.includes('CS')).map((student) => student.split(','));
    const studentsSWE = data.filter((val) => val.includes('SWE')).map((student) => student.split(','));

    console.log(`Number of students: ${data.length}`);
    console.log(
      `Number of students in CS: ${studentsCS.length}. `
      + `List: ${studentsCS.map((val) => val[0]).join(', ')}`,
    );
    console.log(
      `Number of students in SWE: ${studentsSWE.length}. `
      + `List: ${studentsSWE.map((val) => val[0]).join(', ')}`,
    );
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
