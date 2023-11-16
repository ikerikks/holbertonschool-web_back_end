// import HolbertonCourse from "./2-hbtn_course.js";

// test("HolbertonCourse setters are implemented correctly", () => {
//     const course = new HolbertonCourse("PHP", 20, ["Lucie", "Guillaume"]);
//     course.name = "PHP2";
//     course.length = 10;
//     course.students = ["Thomas"];
//     expect(course.name).toBe("PHP2");
//     expect(course.length).toBe(10);
//     expect(course.students).toEqual(["Thomas"]);
// });

import HolbertonCourse from "./2-hbtn_course.js";

test("HolbertonCourse setters are implemented correctly", () => {
    const course = new HolbertonCourse("PHP", 20, ["Lucie", "Guillaume"]);
    course.name = "PHP2";
    course.length = 10;
    course.students = ["Thomas"];
    expect(course.name).toBe("PHP2");
    expect(course.length).toBe(10);
    expect(course.students).toEqual(["Thomas"]);
});