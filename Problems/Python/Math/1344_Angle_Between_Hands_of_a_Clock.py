class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        clock_angle = 360
        clock_scale = 12
        one_hour_angle = 30
        #分针每走一分钟 时针转的角度
        one_minute_h_angle = 30/60
        #分针每走一分钟 分针角度
        one_minute_m_angle = 6
        if hour == 12:
            current_hour = one_minute_h_angle * minutes
        else:
            current_hour = one_hour_angle * hour + one_minute_h_angle * minutes
        current_minute = 6 * minutes
        if abs(current_hour - current_minute) > 180:
            return (360-abs(current_hour - current_minute))
        else:
            return (abs(current_hour - current_minute))
        