class LockDoorCommand implements Command {
  private door: Door;
  constructor(door: Door) {
    this.door = door;
  }
  execute(): void {
    this.door.lock();
  }
}
