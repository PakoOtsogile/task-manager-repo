const { defineConfig } = require('@playwright/test');

module.exports = defineConfig({
  testDir: './LAB 5/tests',
  use: {
    baseURL: 'http://127.0.0.1:3000',
  },
  webServer: {
    command: 'node "LAB 5/server.js"',
    url: 'http://127.0.0.1:3000',
    reuseExistingServer: !process.env.CI,
    timeout: 30_000,
  },
});
