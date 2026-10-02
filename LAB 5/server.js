const { createServer } = require('node:http');
const { readFile } = require('node:fs');
const { join } = require('node:path');

const indexPath = join(__dirname, 'index.html');
const port = Number(process.env.PORT || 3000);

const server = createServer((request, response) => {
  if (request.method !== 'GET' || request.url !== '/') {
    response.writeHead(404, { 'Content-Type': 'text/plain; charset=utf-8' });
    response.end('Not found');
    return;
  }

  readFile(indexPath, (error, content) => {
    if (error) {
      console.error('Unable to read the Task Manager page:', error);
      response.writeHead(500, { 'Content-Type': 'text/plain; charset=utf-8' });
      response.end('Unable to load the Task Manager page.');
      return;
    }

    response.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' });
    response.end(content);
  });
});

server.listen(port, '127.0.0.1', () => {
  console.log(`Task Manager listening at http://127.0.0.1:${port}`);
});
