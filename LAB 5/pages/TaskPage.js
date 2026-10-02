 class TaskPage {
  constructor(page) {
    this.page = page;
    this.taskInput = page.locator('#task-title');
    this.addButton = page.locator('#add-task');
    this.taskList = page.locator('.task-item');
  }

  async goto() {
    await this.page.goto('/');
  }

  async addTask(title) {
    await this.taskInput.fill(title);
    await this.addButton.click();
  }

  async getTaskCount() {
    return await this.taskList.count();
  }
}

module.exports = { TaskPage };
