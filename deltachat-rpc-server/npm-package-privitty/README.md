# @privitty/deltachat-rpc-server

Stdio JSON-RPC server wrapper for npm, published under **@privitty**.

Install with the matching client:

```bash
npm i @privitty/deltachat-rpc-server @privitty/jsonrpc-client
```

```js
import { startDeltaChat } from "@privitty/deltachat-rpc-server";

const dc = await startDeltaChat("deltachat-data");
console.log(await dc.rpc.getSystemInfo());
dc.close();
```

Built from [Privitty/core](https://github.com/Privitty/core). See `.github/workflows/publish-privitty-jsonrpc-client.yml` for `@privitty/jsonrpc-client` publishing.
