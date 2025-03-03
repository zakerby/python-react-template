import { atom } from "jotai";

import { User } from "../types/user";

const userAtom = atom<User | null>(null);
const tokenAtom =  atom<string | null>(null);

export { userAtom, tokenAtom };