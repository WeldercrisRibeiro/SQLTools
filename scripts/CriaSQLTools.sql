use [VMD]
GO

if not exists (select * from master..syslogins where name = N'SQLT')
	EXEC sp_addlogin N'SQLT', N'SQLT@', N'VMD', N'Português'
GO

exec sp_addsrvrolemember N'SQLT', sysadmin
GO


if not exists (select * from sysusers where name = N'SQLT' and uid < 16382)
	EXEC sp_grantdbaccess N'SQLT', N'SQLT'
GO