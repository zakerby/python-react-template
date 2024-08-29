import { useRecoilState } from "recoil";
import { logAtom } from "../state/log";

export const useLogActions = () => {
    const [logs, setLogs] = useRecoilState(logAtom);

    return {logs, setLogs};
}
