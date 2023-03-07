using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Laborator8.domain;

namespace Laborator8.domain.validator
{
    public class EchipaValidator : IValidator<Echipa>
    {
        public void Validate(Echipa e)
        {
            var errors = "";
            if (string.IsNullOrWhiteSpace(e.Nume))
                errors += "Numele echipei trebuie sa fie completat!\n";
            if (e.ID <= 0)
                errors += "Id-ul echipei trebuie sa fie un numar pozitiv!\n";
            if (errors.Length > 0)
                throw new Exception(errors);
        }
    }
}