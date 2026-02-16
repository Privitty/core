# @privitty/deltachat-rpc-server

deltachat-rpc-server (stdio JSON-RPC server) from [Privitty/core](https://github.com/Privitty/core), built from the **dekstop-core** branch and published under **@privitty** on npm.

Same API as `@deltachat/stdio-rpc-server`. Use this when you want the server from the dekstop-core branch.

```bash
npm i @privitty/deltachat-rpc-server @deltachat/jsonrpc-client
```

```js
import { startDeltaChat } from "@privitty/deltachat-rpc-server";

const dc = await startDeltaChat("deltachat-data");
console.log(await dc.rpc.getSystemInfo());
dc.close();
```

Binary is resolved in this order: `DELTA_CHAT_RPC_SERVER` env, PATH (if `takeVersionFromPATH: true`), or platform prebuilds. Node >= 16.
