import { atom } from 'recoil';

const chatAtom = atom({
    key: 'chat_message',
    default: [] as ChatMessage[]
});

export { chatAtom }