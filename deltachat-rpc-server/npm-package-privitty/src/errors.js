//@ts-check
import { ENV_VAR_NAME } from "./const.js";

const cargoInstallCommand =
  "cargo install --git https://github.com/Privitty/core deltachat-rpc-server";

export function NPM_NOT_FOUND_SUPPORTED_PLATFORM_ERROR(package_name) {
  return `deltachat-rpc-server not found:

- Install it with "npm i ${package_name}"
- or put deltachat-rpc-server in your PATH (e.g. "${cargoInstallCommand}")
- or set "${ENV_VAR_NAME}" to the path to the binary"`;
}

export function NPM_NOT_FOUND_UNSUPPORTED_PLATFORM_ERROR() {
  return `deltachat-rpc-server not found: no prebuild for your platform.
Provide the binary via PATH or set "${ENV_VAR_NAME}".`;
}

export function ENV_VAR_LOCATION_NOT_FOUND(error) {
  return `deltachat-rpc-server not found at ${ENV_VAR_NAME}: ${error}`;
}

export function FAILED_TO_START_SERVER_EXECUTABLE(pathToServerBinary, error) {
  return `Failed to start server at '${pathToServerBinary}': ${error}`;
}
