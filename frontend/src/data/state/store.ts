import { atom, createStore } from "jotai";

const appStore = createStore();

const userAtom = atom({});

appStore.set(userAtom, { name: 'John Doe' });

export default appStore;