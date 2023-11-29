from collections import deque

from jeepney import DBusAddress, new_method_call
from jeepney.io.blocking import open_dbus_connection, Proxy
from jeepney.bus_messages import MatchRule, message_bus

import org_freedesktop_portal_desktop

def take_screenshot():
  sc_int = DBusAddress('/org/freedesktop/portal/desktop',
                              bus_name='org.freedesktop.portal.Desktop',
                              interface='org.freedesktop.portal.Screenshot')

  with open_dbus_connection() as conn:
    sc_proxy = Proxy(org_freedesktop_portal_desktop.Screenshot(), conn)
    request_token, = sc_proxy.Screenshot("", {})
    print(request_token)

    match_rule = MatchRule(
      type="signal",
      path=sc_int.object_path,
      interface="org.freedesktop.portal.Request",
    )

    with conn.filter(match_rule) as queue:
      signal_msg = conn.recv_until_filtered(queue)
      print(signal_msg)
