default['influxdb-url'] =  "http://127.0.0.1:8086/db/"
default['grafana']['datasources'] = { 'influxdb'=> {
                                        'type'=>"'influxdb'",
                                        'url'=> "'#{default['influxdb-url']}collectd'",
                                        'username'=> "'collectd'",
                                        'password'=> "'collectd'"
                                      },
                                      'grafana'=> {
                                        'type'=> "'influxdb'",
                                        'url'=> "'#{default['influxdb-url']}grafana'",
                                        'username'=> "'grafana'",
                                        'password'=> "'grafana'",
                                        'grafanaDB'=> true
                                      }
}
default[:collectd][:pkg_name] = "collectd"
