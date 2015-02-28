#
# Cookbook Name:: eucatelemetry
# Recipe:: default
#
# Copyright (C) 2014
#
#
#
include_recipe 'grafana'
include_recipe 'influxdb'
include_recipe 'supervisor'
package 'golang'
package 'git'
package 'collectd'

proxy_path = "/opt/influxdb-collectd-proxy"
git proxy_path do
  repository "https://github.com/hoonmin/influxdb-collectd-proxy.git"
  action :sync
end

execute 'export GOPATH=/opt/influxdb-collectd-proxy/; go get github.com/tools/godep; ./bin/godep restore' do
  cwd proxy_path
end

execute "make" do
  cwd proxy_path
end

supervisor_service "influxdb-collectd-proxy" do
  command "#{proxy_path}/bin/influxdb-collectd-proxy --typesdb='/usr/share/collectd/types.db' --database='collectd' --username='collectd' --password='collectd'"
end

### Create DBs
%w{grafana collectd}.each do |name|
  execute "curl -X POST 'http://localhost:8086/db?u=root&p=root' -d '{\"name\": \"#{name}\"}'"
  execute "curl -X POST 'http://localhost:8086/db/#{name}/users?u=root&p=root' -d '{\"name\": \"#{name}\", \"password\": \"#{name}\"}'"
end

template "/srv/apps/grafana/app/dashboards/default.json" do
  source "default.json.erb"
end
