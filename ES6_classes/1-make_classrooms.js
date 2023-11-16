import ClassRoom from "./0-classroom";

export default ClassRoom.initializeRooms = function() {
  return [new ClassRoom(19), new ClassRoom(24), new ClassRoom(34)];
}
