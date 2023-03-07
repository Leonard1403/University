using System.Text;
using Laborator8.domain;
using Laborator8.domain.validator;

namespace Laborator8.validator
{
    class ElevValidator : IValidator<Elev>
    {
        public void Validate(Elev elev)
        {
            StringBuilder errors = new StringBuilder();
            if (elev.ID <= 0)
                errors.Append("ID-ul elevului nu poate fi mai mic sau egal cu 0!\n");
            if (elev.Nume == null || elev.Nume.Trim().Equals(""))
                errors.Append("Numele elevului nu poate fi null sau gol!\n");
            if (elev.Scoala == null || elev.Scoala.Trim().Equals(""))
                errors.Append("Scoala elevului nu poate fi null sau goala!\n");
            if (errors.Length > 0)
                throw new ValidationException(errors.ToString());
        }
    }
}