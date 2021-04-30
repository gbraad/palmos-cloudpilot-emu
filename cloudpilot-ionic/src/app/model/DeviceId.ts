export enum DeviceId {
    palmV = 'PalmV',
    iiic = 'PalmIIIc',
    m515 = 'PalmM515',
    m130 = 'PalmM130',
}

export function isColor(deviceId: DeviceId | undefined): boolean {
    return deviceId !== DeviceId.palmV;
}
