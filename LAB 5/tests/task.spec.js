 const { test, expect } = require('@playwright/test');
const { TaskPage } = require('../pages/TaskPage');
const testData = require('../../test-data/tasks.json');

test.describe('Task Manager', () => {
  testData.forEach((data, index) => {
    test(`Add task: ${data.title}`, async ({ page }) => {
      const taskPage = new TaskPage(page);
      await taskPage.goto();
      await taskPage.addTask(data.title);
      await expect(page.locator('.task-item')).toHaveText(data.title);
    });
  });
});
