import {useAtom} from 'jotai';
import { logAtom } from "../state/log";

export const useLogActions = () => {
    const [logs, setLogs] = useAtom(logAtom);

    return {logs, setLogs};
}
