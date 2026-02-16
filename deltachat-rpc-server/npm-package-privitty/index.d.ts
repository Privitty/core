import { StdioDeltaChat } from "@deltachat/jsonrpc-client";

export interface SearchOptions {
  takeVersionFromPATH: boolean;
  disableEnvPath: boolean;
}

export function getRPCServerPath(
  options?: Partial<SearchOptions>
): Promise<string>;

export type DeltaChatOverJsonRpcServer = StdioDeltaChat & {
  readonly pathToServerBinary: string;
};

export interface StartOptions {
  muteStdErr: boolean;
}

export function startDeltaChat(
  directory: string,
  options?: Partial<SearchOptions & StartOptions>
): Promise<DeltaChatOverJsonRpcServer>;

export namespace FnTypes {
  export type getRPCServerPath = typeof getRPCServerPath;
  export type startDeltaChat = typeof startDeltaChat;
}
